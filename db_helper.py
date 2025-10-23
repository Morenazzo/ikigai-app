"""
Simple database helper compatible with Vercel serverless.
Replaces cs50.SQL with a lightweight SQLAlchemy wrapper.
"""
from sqlalchemy import create_engine, text
from sqlalchemy.pool import NullPool


class SQL:
    """Database wrapper compatible with cs50.SQL interface"""
    
    def __init__(self, url):
        """Initialize database connection"""
        # Use NullPool for serverless (connections don't persist)
        self.engine = create_engine(
            url,
            poolclass=NullPool,
            connect_args={'check_same_thread': False} if url.startswith('sqlite') else {}
        )
    
    def execute(self, query, *args):
        """
        Execute a SQL query and return results.
        Compatible with cs50.SQL.execute() interface.
        
        Args:
            query: SQL query string (can use ? or :name placeholders)
            *args: Positional parameters for ? placeholders
        
        Returns:
            For SELECT: list of dicts
            For INSERT/UPDATE/DELETE: rowcount
        """
        with self.engine.connect() as conn:
            trans = conn.begin()
            try:
                # Convert ? placeholders to numbered parameters for SQLAlchemy
                if args and '?' in query:
                    # Replace ? with :param0, :param1, etc.
                    param_names = []
                    for i in range(len(args)):
                        param_names.append(f'param{i}')
                        query = query.replace('?', f':param{i}', 1)
                    
                    # Create parameter dict
                    params = {f'param{i}': arg for i, arg in enumerate(args)}
                else:
                    params = {}
                
                result = conn.execute(text(query), params)
                trans.commit()
                
                # If it's a SELECT query, return rows as dicts
                query_upper = query.strip().upper()
                if query_upper.startswith('SELECT'):
                    rows = result.fetchall()
                    # Convert to list of dicts
                    if rows:
                        return [dict(row._mapping) for row in rows]
                    return []
                else:
                    # For INSERT/UPDATE/DELETE, return rowcount
                    return result.rowcount
                    
            except Exception as e:
                trans.rollback()
                # Re-raise with more context
                raise Exception(f"Database error: {str(e)}\nQuery: {query}\nArgs: {args}") from e
