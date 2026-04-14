from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(500))
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return f'<Order {self.id} by User {self.user_id}>'

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User')

    def __repr__(self):
        return f'<Message {self.id} from User {self.user_id}>'

