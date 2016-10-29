# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, Index, Integer, SmallInteger, String, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Bug(Base):
    __tablename__ = 'bug'
    __table_args__ = (
        Index('bug', 'product', 'module', 'project', 'assignedTo'),
    )

    id = Column(Integer, primary_key=True)
    product = Column(Integer, nullable=False, server_default=text("'0'"))
    branch = Column(Integer, nullable=False, server_default=text("'0'"))
    module = Column(Integer, nullable=False, server_default=text("'0'"))
    project = Column(Integer, nullable=False, server_default=text("'0'"))
    plan = Column(Integer, nullable=False, server_default=text("'0'"))
    story = Column(Integer, nullable=False, server_default=text("'0'"))
    storyVersion = Column(SmallInteger, nullable=False, server_default=text("'1'"))
    task = Column(Integer, nullable=False, server_default=text("'0'"))
    toTask = Column(Integer, nullable=False, server_default=text("'0'"))
    toStory = Column(Integer, nullable=False, server_default=text("'0'"))
    title = Column(String(255), nullable=False)
    keywords = Column(String(255), nullable=False)
    severity = Column(Integer, nullable=False, server_default=text("'0'"))
    pri = Column(Integer, nullable=False)
    type = Column(String(30), nullable=False, server_default=text("''"))
    os = Column(String(30), nullable=False, server_default=text("''"))
    browser = Column(String(30), nullable=False, server_default=text("''"))
    hardware = Column(String(30), nullable=False)
    found = Column(String(30), nullable=False, server_default=text("''"))
    steps = Column(Text, nullable=False)
    status = Column(Enum(u'active', u'resolved', u'closed'), nullable=False, server_default=text("'active'"))
    color = Column(String(7), nullable=False)
    confirmed = Column(Integer, nullable=False, server_default=text("'0'"))
    activatedCount = Column(SmallInteger, nullable=False)
    mailto = Column(String(255), nullable=False, server_default=text("''"))
    openedBy = Column(String(30), nullable=False, server_default=text("''"))
    openedDate = Column(DateTime, nullable=False)
    openedBuild = Column(String(255), nullable=False)
    assignedTo = Column(String(30), nullable=False, server_default=text("''"))
    assignedDate = Column(DateTime, nullable=False)
    resolvedBy = Column(String(30), nullable=False, server_default=text("''"))
    resolution = Column(String(30), nullable=False, server_default=text("''"))
    resolvedBuild = Column(String(30), nullable=False, server_default=text("''"))
    resolvedDate = Column(DateTime, nullable=False)
    closedBy = Column(String(30), nullable=False, server_default=text("''"))
    closedDate = Column(DateTime, nullable=False)
    duplicateBug = Column(Integer, nullable=False)
    linkBug = Column(String(255), nullable=False)
    case = Column(Integer, nullable=False)
    caseVersion = Column(SmallInteger, nullable=False, server_default=text("'1'"))
    result = Column(Integer, nullable=False)
    testtask = Column(Integer, nullable=False)
    lastEditedBy = Column(String(30), nullable=False, server_default=text("''"))
    lastEditedDate = Column(DateTime, nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Doc(Base):
    __tablename__ = 'doc'
    __table_args__ = (
        Index('doc', 'product', 'project'),
    )

    id = Column(Integer, primary_key=True)
    product = Column(Integer, nullable=False)
    project = Column(Integer, nullable=False)
    lib = Column(String(30), nullable=False)
    module = Column(String(30), nullable=False)
    title = Column(String(255), nullable=False)
    digest = Column(String(255), nullable=False)
    keywords = Column(String(255), nullable=False)
    type = Column(String(30), nullable=False)
    content = Column(Text, nullable=False)
    url = Column(String(255), nullable=False)
    views = Column(SmallInteger, nullable=False)
    addedBy = Column(String(30), nullable=False)
    addedDate = Column(DateTime, nullable=False)
    editedBy = Column(String(30), nullable=False)
    editedDate = Column(DateTime, nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))
