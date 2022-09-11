"""OK this is a code file that helps us create the database model"""
from dataclasses import dataclass


class Person:
    """It stores the information of n person"""
    id: int
    name: str
    surname: str


class Account:
    """It stores the information of their account"""
    account_number: int
    account_balance: int


class Attendence:
    """Store when they sign in for work"""
    timestamp: int
    id: int
