from datetime import datetime

from sqlalchemy import (JSON, Boolean, Column, DateTime, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship

from app.core.db.base import Base


class CalculationHistory(Base):
    """
    Модель для хранения истории вычислений
    """

    __tablename__ = "calculation_history"

    id = Column(Integer, primary_key=True)
    dataset_file_name = Column(String(100), nullable=False)
    calculation_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    success = Column(Boolean, nullable=False, default=False)
    result = Column(JSON, nullable=True)
    errors = Column(JSON, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref="calculation_history")
