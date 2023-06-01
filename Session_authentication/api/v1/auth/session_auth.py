#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    '''
    '''
    pass

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if user_id is None or not isinstance(user_id, str):
            return None
        session_uuid = str(uuid.uuid4())
        self.user_id_by_session_id[session_uuid] = user_id
        return session_uuid