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
        """
        with self.engine.connect() as conn:
            # Start a transaction
            trans = conn.begin()
            try:
                # Convert ? placeholders to :1, :2, etc. for SQLAlchemy
                if '?' in query:
                    # Count placeholders
                    param_count = query.count('?')
                    # Replace with named parameters
                    for i in range(param_count):
                        query = query.replace('?', f':param{i}', 1)
                    # Create dict of parameters
                    params = {f'param{i}': arg for i, arg in enumerate(args)}
                else:
                    params = {}
                
                result = conn.execute(text(query), params)
                trans.commit()
                
                # If it's a SELECT query, return rows as dicts
                if query.strip().upper().startswith('SELECT'):
                    rows = result.fetchall()
                    # Convert to list of dicts
                    return [dict(row._mapping) for row in rows]
                else:
                    # For INSERT/UPDATE/DELETE, return rowcount
                    return result.rowcount
                    
            except Exception as e:
                trans.rollback()
                raise e

