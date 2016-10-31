# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Enum, Float, Index, Integer, SmallInteger, String, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base

from app import db


class Action(db.Model):
    __tablename__ = 'action'
    __table_args__ = (
        Index('action', 'objectID', 'product', 'project', 'action', 'date'),
    )

    id = Column(Integer, primary_key=True)
    objectType = Column(String(30), nullable=False, server_default=text("''"))
    objectID = Column(Integer, nullable=False, server_default=text("'0'"))
    product = Column(String(255), nullable=False)
    project = Column(Integer, nullable=False)
    actor = Column(String(30), nullable=False, server_default=text("''"))
    action = Column(String(30), nullable=False, server_default=text("''"))
    date = Column(DateTime, nullable=False)
    comment = Column(Text, nullable=False)
    extra = Column(Text, nullable=False)
    read = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Block(db.Model):
    __tablename__ = 'block'
    __table_args__ = (
        Index('block', 'account', 'module'),
        Index('accountModuleOrder', 'account', 'module', 'order', unique=True)
    )

    id = Column(Integer, primary_key=True)
    account = Column(String(30), nullable=False)
    module = Column(String(20), nullable=False)
    title = Column(String(100), nullable=False)
    source = Column(String(20), nullable=False)
    block = Column(String(20), nullable=False)
    params = Column(Text, nullable=False)
    order = Column(Integer, nullable=False, server_default=text("'0'"))
    grid = Column(Integer, nullable=False, server_default=text("'0'"))
    hidden = Column(Integer, nullable=False, server_default=text("'0'"))


class Branch(db.Model):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True)
    product = Column(Integer, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Bug(db.Model):
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


class Build(db.Model):
    __tablename__ = 'build'
    __table_args__ = (
        Index('build', 'product', 'project'),
    )

    id = Column(Integer, primary_key=True)
    product = Column(Integer, nullable=False, server_default=text("'0'"))
    branch = Column(Integer, nullable=False, server_default=text("'0'"))
    project = Column(Integer, nullable=False, server_default=text("'0'"))
    name = Column(String(150), nullable=False)
    scmPath = Column(String(255), nullable=False)
    filePath = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    stories = Column(Text, nullable=False)
    bugs = Column(Text, nullable=False)
    builder = Column(String(30), nullable=False, server_default=text("''"))
    desc = Column(Text, nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Burn(db.Model):
    __tablename__ = 'burn'

    project = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, primary_key=True, nullable=False)
    left = Column(Float, nullable=False)
    consumed = Column(Float, nullable=False)


class Case(db.Model):
    __tablename__ = 'case'
    __table_args__ = (
        Index('case', 'product', 'module', 'story'),
    )

    id = Column(Integer, primary_key=True)
    product = Column(Integer, nullable=False, server_default=text("'0'"))
    branch = Column(Integer, nullable=False, server_default=text("'0'"))
    module = Column(Integer, nullable=False, server_default=text("'0'"))
    path = Column(Integer, nullable=False, server_default=text("'0'"))
    story = Column(Integer, nullable=False, server_default=text("'0'"))
    storyVersion = Column(SmallInteger, nullable=False, server_default=text("'1'"))
    title = Column(String(255), nullable=False)
    precondition = Column(Text, nullable=False)
    keywords = Column(String(255), nullable=False)
    pri = Column(Integer, nullable=False, server_default=text("'3'"))
    type = Column(String(30), nullable=False, server_default=text("'1'"))
    stage = Column(String(255), nullable=False)
    howRun = Column(String(30), nullable=False)
    scriptedBy = Column(String(30), nullable=False)
    scriptedDate = Column(Date, nullable=False)
    scriptStatus = Column(String(30), nullable=False)
    scriptLocation = Column(String(255), nullable=False)
    status = Column(String(30), nullable=False, server_default=text("'1'"))
    color = Column(String(7), nullable=False)
    frequency = Column(Enum(u'1', u'2', u'3'), nullable=False, server_default=text("'1'"))
    order = Column(Integer, nullable=False, server_default=text("'0'"))
    openedBy = Column(String(30), nullable=False, server_default=text("''"))
    openedDate = Column(DateTime, nullable=False)
    lastEditedBy = Column(String(30), nullable=False, server_default=text("''"))
    lastEditedDate = Column(DateTime, nullable=False)
    version = Column(Integer, nullable=False, server_default=text("'0'"))
    linkCase = Column(String(255), nullable=False)
    fromBug = Column(Integer, nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))
    lastRunner = Column(String(30), nullable=False)
    lastRunDate = Column(DateTime, nullable=False)
    lastRunResult = Column(String(30), nullable=False)


class Casestep(db.Model):
    __tablename__ = 'casestep'
    __table_args__ = (
        Index('case', 'case', 'version'),
    )

    id = Column(Integer, primary_key=True)
    case = Column(Integer, nullable=False, server_default=text("'0'"))
    version = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    desc = Column(Text, nullable=False)
    expect = Column(Text, nullable=False)


class Company(db.Model):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    phone = Column(String(20))
    fax = Column(String(20))
    address = Column(String(120))
    zipcode = Column(String(10))
    website = Column(String(120))
    backyard = Column(String(120))
    guest = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    admins = Column(String(255))
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Config(db.Model):
    __tablename__ = 'config'
    __table_args__ = (
        Index('unique', 'owner', 'module', 'section', 'key', unique=True),
    )

    id = Column(Integer, primary_key=True)
    owner = Column(String(30), nullable=False, server_default=text("''"))
    module = Column(String(30), nullable=False)
    section = Column(String(30), nullable=False, server_default=text("''"))
    key = Column(String(30), nullable=False, server_default=text("''"))
    value = Column(Text, nullable=False)


class Cron(db.Model):
    __tablename__ = 'cron'

    id = Column(Integer, primary_key=True)
    m = Column(String(20), nullable=False)
    h = Column(String(20), nullable=False)
    dom = Column(String(20), nullable=False)
    mon = Column(String(20), nullable=False)
    dow = Column(String(20), nullable=False)
    command = Column(Text, nullable=False)
    remark = Column(String(255), nullable=False)
    type = Column(String(20), nullable=False)
    buildin = Column(Integer, nullable=False, server_default=text("'0'"))
    status = Column(String(20), nullable=False)
    lastTime = Column(DateTime, nullable=False, index=True)


class Dept(db.Model):
    __tablename__ = 'dept'
    __table_args__ = (
        Index('dept', 'parent', 'path'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    parent = Column(Integer, nullable=False, server_default=text("'0'"))
    path = Column(String(255), nullable=False, server_default=text("''"))
    grade = Column(Integer, nullable=False, server_default=text("'0'"))
    order = Column(Integer, nullable=False, server_default=text("'0'"))
    position = Column(String(30), nullable=False, server_default=text("''"))
    function = Column(String(255), nullable=False, server_default=text("''"))
    manager = Column(String(30), nullable=False, server_default=text("''"))


class Doc(db.Model):
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


class Doclib(db.Model):
    __tablename__ = 'doclib'

    id = Column(SmallInteger, primary_key=True)
    name = Column(String(60), nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Effort(db.Model):
    __tablename__ = 'effort'

    id = Column(Integer, primary_key=True)
    user = Column(String(30), nullable=False, index=True, server_default=text("''"))
    todo = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'1'"))
    date = Column(Date, nullable=False)
    begin = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    end = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    type = Column(Enum(u'1', u'2', u'3'), nullable=False, server_default=text("'1'"))
    idvalue = Column(Integer, nullable=False, server_default=text("'0'"))
    name = Column(String(30), nullable=False, server_default=text("''"))
    desc = Column(String(255), nullable=False, server_default=text("''"))
    status = Column(Enum(u'1', u'2', u'3'), nullable=False, server_default=text("'1'"))


class Extension(db.Model):
    __tablename__ = 'extension'
    __table_args__ = (
        Index('extension', 'name', 'installedTime'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    code = Column(String(30), nullable=False, unique=True)
    version = Column(String(50), nullable=False)
    author = Column(String(100), nullable=False)
    desc = Column(Text, nullable=False)
    license = Column(Text, nullable=False)
    type = Column(String(20), nullable=False, server_default=text("'extension'"))
    site = Column(String(150), nullable=False)
    zentaoCompatible = Column(String(100), nullable=False)
    installedTime = Column(DateTime, nullable=False)
    depends = Column(String(100), nullable=False)
    dirs = Column(Text, nullable=False)
    files = Column(Text, nullable=False)
    status = Column(String(20), nullable=False)


class File(db.Model):
    __tablename__ = 'file'
    __table_args__ = (
        Index('file', 'objectType', 'objectID'),
    )

    id = Column(Integer, primary_key=True)
    pathname = Column(String(50), nullable=False)
    title = Column(String(90), nullable=False)
    extension = Column(String(30), nullable=False)
    size = Column(Integer, nullable=False, server_default=text("'0'"))
    objectType = Column(String(30), nullable=False)
    objectID = Column(Integer, nullable=False)
    addedBy = Column(String(30), nullable=False, server_default=text("''"))
    addedDate = Column(DateTime, nullable=False)
    downloads = Column(Integer, nullable=False, server_default=text("'0'"))
    extra = Column(String(255), nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Group(db.Model):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    role = Column(String(30), nullable=False, server_default=text("''"))
    desc = Column(String(255), nullable=False, server_default=text("''"))
    acl = Column(Text, nullable=False)


t_grouppriv = Table(
    'grouppriv', metadata,
    Column('group', Integer, nullable=False, server_default=text("'0'")),
    Column('module', String(30), nullable=False, server_default=text("''")),
    Column('method', String(30), nullable=False, server_default=text("''")),
    Index('group', 'group', 'module', 'method', unique=True)
)


class History(db.Model):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    action = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    field = Column(String(30), nullable=False, server_default=text("''"))
    old = Column(Text, nullable=False)
    new = Column(Text, nullable=False)
    diff = Column(String, nullable=False)


class Lang(db.Model):
    __tablename__ = 'lang'
    __table_args__ = (
        Index('lang', 'lang', 'module', 'section', 'key', unique=True),
    )

    id = Column(Integer, primary_key=True)
    lang = Column(String(30), nullable=False)
    module = Column(String(30), nullable=False)
    section = Column(String(30), nullable=False)
    key = Column(String(60), nullable=False)
    value = Column(Text, nullable=False)
    system = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'1'"))


class Mailqueue(db.Model):
    __tablename__ = 'mailqueue'

    id = Column(Integer, primary_key=True)
    toList = Column(String(255), nullable=False)
    ccList = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    addedBy = Column(String(30), nullable=False)
    addedDate = Column(DateTime, nullable=False)
    sendTime = Column(DateTime, nullable=False, index=True)
    status = Column(String(10), nullable=False, server_default=text("'wait'"))
    failReason = Column(Text, nullable=False)


class Module(db.Model):
    __tablename__ = 'module'
    __table_args__ = (
        Index('module', 'root', 'type', 'path'),
    )

    id = Column(Integer, primary_key=True)
    root = Column(Integer, nullable=False, server_default=text("'0'"))
    branch = Column(Integer, nullable=False, server_default=text("'0'"))
    name = Column(String(60), nullable=False, server_default=text("''"))
    parent = Column(Integer, nullable=False, server_default=text("'0'"))
    path = Column(String(255), nullable=False, server_default=text("''"))
    grade = Column(Integer, nullable=False, server_default=text("'0'"))
    order = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    type = Column(String(30), nullable=False)
    owner = Column(String(30), nullable=False)
    short = Column(String(30), nullable=False)


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(90), nullable=False)
    code = Column(String(45), nullable=False)
    type = Column(String(30), nullable=False, server_default=text("'normal'"))
    status = Column(String(30), nullable=False, server_default=text("''"))
    desc = Column(Text, nullable=False)
    PO = Column(String(30), nullable=False)
    QD = Column(String(30), nullable=False)
    RD = Column(String(30), nullable=False)
    acl = Column(Enum(u'open', u'private', u'custom'), nullable=False, server_default=text("'open'"))
    whitelist = Column(String(255), nullable=False)
    createdBy = Column(String(30), nullable=False)
    createdDate = Column(DateTime, nullable=False)
    createdVersion = Column(String(20), nullable=False)
    order = Column(Integer, nullable=False, index=True)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Productplan(db.Model):
    __tablename__ = 'productplan'
    __table_args__ = (
        Index('plan', 'product', 'end'),
    )

    id = Column(Integer, primary_key=True)
    product = Column(Integer, nullable=False)
    branch = Column(Integer, nullable=False)
    title = Column(String(90), nullable=False)
    desc = Column(Text, nullable=False)
    begin = Column(Date, nullable=False)
    end = Column(Date, nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Project(db.Model):
    __tablename__ = 'project'
    __table_args__ = (
        Index('project', 'parent', 'begin', 'end', 'status', 'order'),
    )

    id = Column(Integer, primary_key=True)
    isCat = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    catID = Column(Integer, nullable=False)
    type = Column(String(20), nullable=False, server_default=text("'sprint'"))
    parent = Column(Integer, nullable=False, server_default=text("'0'"))
    name = Column(String(90), nullable=False)
    code = Column(String(45), nullable=False)
    begin = Column(Date, nullable=False)
    end = Column(Date, nullable=False)
    days = Column(SmallInteger, nullable=False)
    status = Column(String(10), nullable=False)
    statge = Column(Enum(u'1', u'2', u'3', u'4', u'5'), nullable=False, server_default=text("'1'"))
    pri = Column(Enum(u'1', u'2', u'3', u'4'), nullable=False, server_default=text("'1'"))
    desc = Column(Text, nullable=False)
    openedBy = Column(String(30), nullable=False, server_default=text("''"))
    openedDate = Column(Integer, nullable=False, server_default=text("'0'"))
    openedVersion = Column(String(20), nullable=False)
    closedBy = Column(String(30), nullable=False, server_default=text("''"))
    closedDate = Column(Integer, nullable=False, server_default=text("'0'"))
    canceledBy = Column(String(30), nullable=False, server_default=text("''"))
    canceledDate = Column(Integer, nullable=False, server_default=text("'0'"))
    PO = Column(String(30), nullable=False, server_default=text("''"))
    PM = Column(String(30), nullable=False, server_default=text("''"))
    QD = Column(String(30), nullable=False, server_default=text("''"))
    RD = Column(String(30), nullable=False, server_default=text("''"))
    team = Column(String(30), nullable=False)
    acl = Column(Enum(u'open', u'private', u'custom'), nullable=False, server_default=text("'open'"))
    whitelist = Column(String(255), nullable=False)
    order = Column(Integer, nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Projectproduct(db.Model):
    __tablename__ = 'projectproduct'

    project = Column(Integer, primary_key=True, nullable=False)
    product = Column(Integer, primary_key=True, nullable=False)
    branch = Column(Integer, nullable=False)


t_projectstory = Table(
    'projectstory', metadata,
    Column('project', Integer, nullable=False, server_default=text("'0'")),
    Column('product', Integer, nullable=False),
    Column('story', Integer, nullable=False, server_default=text("'0'")),
    Column('version', SmallInteger, nullable=False, server_default=text("'1'")),
    Index('project', 'project', 'story', unique=True)
)


class Release(db.Model):
    __tablename__ = 'release'

    id = Column(Integer, primary_key=True)
    product = Column(Integer, nullable=False, server_default=text("'0'"))
    branch = Column(Integer, nullable=False, server_default=text("'0'"))
    build = Column(Integer, nullable=False, index=True)
    name = Column(String(30), nullable=False, server_default=text("''"))
    date = Column(Date, nullable=False)
    stories = Column(Text, nullable=False)
    bugs = Column(Text, nullable=False)
    leftBugs = Column(Text, nullable=False)
    desc = Column(Text, nullable=False)
    status = Column(String(20), nullable=False, server_default=text("'normal'"))
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Story(db.Model):
    __tablename__ = 'story'
    __table_args__ = (
        Index('story', 'product', 'module', 'status', 'assignedTo'),
    )

    id = Column(Integer, primary_key=True)
    product = Column(Integer, nullable=False, server_default=text("'0'"))
    branch = Column(Integer, nullable=False, server_default=text("'0'"))
    module = Column(Integer, nullable=False, server_default=text("'0'"))
    plan = Column(Text, nullable=False)
    source = Column(String(20), nullable=False)
    sourceNote = Column(String(255), nullable=False)
    fromBug = Column(Integer, nullable=False, server_default=text("'0'"))
    title = Column(String(255), nullable=False)
    keywords = Column(String(255), nullable=False)
    type = Column(String(30), nullable=False, server_default=text("''"))
    pri = Column(Integer, nullable=False, server_default=text("'3'"))
    estimate = Column(Float, nullable=False)
    status = Column(Enum(u'', u'changed', u'active', u'draft', u'closed'), nullable=False, server_default=text("''"))
    color = Column(String(7), nullable=False)
    stage = Column(Enum(u'', u'wait', u'planned', u'projected', u'developing', u'developed', u'testing', u'tested', u'verified', u'released'), nullable=False, server_default=text("'wait'"))
    mailto = Column(String(255), nullable=False, server_default=text("''"))
    openedBy = Column(String(30), nullable=False, server_default=text("''"))
    openedDate = Column(DateTime, nullable=False)
    assignedTo = Column(String(30), nullable=False, server_default=text("''"))
    assignedDate = Column(DateTime, nullable=False)
    lastEditedBy = Column(String(30), nullable=False, server_default=text("''"))
    lastEditedDate = Column(DateTime, nullable=False)
    reviewedBy = Column(String(255), nullable=False)
    reviewedDate = Column(Date, nullable=False)
    closedBy = Column(String(30), nullable=False, server_default=text("''"))
    closedDate = Column(DateTime, nullable=False)
    closedReason = Column(String(30), nullable=False)
    toBug = Column(Integer, nullable=False)
    childStories = Column(String(255), nullable=False)
    linkStories = Column(String(255), nullable=False)
    duplicateStory = Column(Integer, nullable=False)
    version = Column(SmallInteger, nullable=False, server_default=text("'1'"))
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


t_storyspec = Table(
    'storyspec', metadata,
    Column('story', Integer, nullable=False),
    Column('version', SmallInteger, nullable=False),
    Column('title', String(90), nullable=False),
    Column('spec', Text, nullable=False),
    Column('verify', Text, nullable=False),
    Index('story', 'story', 'version', unique=True)
)


t_storystage = Table(
    'storystage', metadata,
    Column('story', Integer, nullable=False, index=True),
    Column('branch', Integer, nullable=False),
    Column('stage', String(50), nullable=False)
)


class Task(db.Model):
    __tablename__ = 'task'
    __table_args__ = (
        Index('task', 'project', 'module', 'story', 'assignedTo'),
    )

    id = Column(Integer, primary_key=True)
    project = Column(Integer, nullable=False, server_default=text("'0'"))
    module = Column(Integer, nullable=False, server_default=text("'0'"))
    story = Column(Integer, nullable=False, server_default=text("'0'"))
    storyVersion = Column(SmallInteger, nullable=False, server_default=text("'1'"))
    fromBug = Column(Integer, nullable=False, server_default=text("'0'"))
    name = Column(String(255), nullable=False)
    type = Column(String(20), nullable=False)
    pri = Column(Integer, nullable=False, server_default=text("'0'"))
    estimate = Column(Float, nullable=False)
    consumed = Column(Float, nullable=False)
    left = Column(Float, nullable=False)
    deadline = Column(Date, nullable=False)
    status = Column(Enum(u'wait', u'doing', u'done', u'pause', u'cancel', u'closed'), nullable=False, server_default=text("'wait'"))
    color = Column(String(7), nullable=False)
    mailto = Column(String(255), nullable=False, server_default=text("''"))
    desc = Column(Text, nullable=False)
    openedBy = Column(String(30), nullable=False)
    openedDate = Column(DateTime, nullable=False)
    assignedTo = Column(String(30), nullable=False)
    assignedDate = Column(DateTime, nullable=False)
    estStarted = Column(Date, nullable=False)
    realStarted = Column(Date, nullable=False)
    finishedBy = Column(String(30), nullable=False)
    finishedDate = Column(DateTime, nullable=False)
    canceledBy = Column(String(30), nullable=False)
    canceledDate = Column(DateTime, nullable=False)
    closedBy = Column(String(30), nullable=False)
    closedDate = Column(DateTime, nullable=False)
    closedReason = Column(String(30), nullable=False)
    lastEditedBy = Column(String(30), nullable=False)
    lastEditedDate = Column(DateTime, nullable=False)
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Taskestimate(db.Model):
    __tablename__ = 'taskestimate'

    id = Column(Integer, primary_key=True)
    task = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    date = Column(Date, nullable=False)
    left = Column(Float, nullable=False, server_default=text("'0'"))
    consumed = Column(Float, nullable=False)
    account = Column(String(30), nullable=False, server_default=text("''"))
    work = Column(String(255), nullable=False)


class Team(db.Model):
    __tablename__ = 'team'

    project = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    account = Column(String(30), primary_key=True, nullable=False, server_default=text("''"))
    role = Column(String(30), nullable=False, server_default=text("''"))
    join = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    days = Column(SmallInteger, nullable=False)
    hours = Column(Float(2), nullable=False, server_default=text("'0.0'"))


class Testresult(db.Model):
    __tablename__ = 'testresult'
    __table_args__ = (
        Index('testresult', 'case', 'version', 'run'),
    )

    id = Column(Integer, primary_key=True)
    run = Column(Integer, nullable=False)
    case = Column(Integer, nullable=False)
    version = Column(SmallInteger, nullable=False)
    caseResult = Column(String(30), nullable=False)
    stepResults = Column(Text, nullable=False)
    lastRunner = Column(String(30), nullable=False)
    date = Column(DateTime, nullable=False)


class Testrun(db.Model):
    __tablename__ = 'testrun'
    __table_args__ = (
        Index('task', 'task', 'case', unique=True),
    )

    id = Column(Integer, primary_key=True)
    task = Column(Integer, nullable=False, server_default=text("'0'"))
    case = Column(Integer, nullable=False, server_default=text("'0'"))
    version = Column(Integer, nullable=False, server_default=text("'0'"))
    assignedTo = Column(String(30), nullable=False, server_default=text("''"))
    lastRunner = Column(String(30), nullable=False)
    lastRunDate = Column(DateTime, nullable=False)
    lastRunResult = Column(String(30), nullable=False)
    status = Column(String(30), nullable=False)


class Testtask(db.Model):
    __tablename__ = 'testtask'

    id = Column(Integer, primary_key=True)
    name = Column(String(90), nullable=False)
    product = Column(Integer, nullable=False)
    project = Column(Integer, nullable=False, server_default=text("'0'"))
    build = Column(String(30), nullable=False, index=True)
    owner = Column(String(30), nullable=False)
    pri = Column(Integer, nullable=False, server_default=text("'0'"))
    begin = Column(Date, nullable=False)
    end = Column(Date, nullable=False)
    mailto = Column(String(255), nullable=False, server_default=text("''"))
    desc = Column(Text, nullable=False)
    report = Column(Text, nullable=False)
    status = Column(Enum(u'blocked', u'doing', u'wait', u'done'), nullable=False, server_default=text("'wait'"))
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Todo(db.Model):
    __tablename__ = 'todo'
    __table_args__ = (
        Index('todo', 'account', 'date'),
    )

    id = Column(Integer, primary_key=True)
    account = Column(String(30), nullable=False)
    date = Column(Date, nullable=False)
    begin = Column(SmallInteger, nullable=False)
    end = Column(SmallInteger, nullable=False)
    type = Column(String(10), nullable=False)
    idvalue = Column(Integer, nullable=False, server_default=text("'0'"))
    pri = Column(Integer, nullable=False)
    name = Column(String(150), nullable=False)
    desc = Column(Text, nullable=False)
    status = Column(Enum(u'wait', u'doing', u'done'), nullable=False, server_default=text("'wait'"))
    private = Column(Integer, nullable=False)


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = (
        Index('user', 'dept', 'email', 'commiter'),
    )

    id = Column(Integer, primary_key=True)
    dept = Column(Integer, nullable=False, server_default=text("'0'"))
    account = Column(String(30), nullable=False, unique=True, server_default=text("''"))
    password = Column(String(32), nullable=False, server_default=text("''"))
    role = Column(String(10), nullable=False, server_default=text("''"))
    realname = Column(String(30), nullable=False, server_default=text("''"))
    nickname = Column(String(60), nullable=False, server_default=text("''"))
    commiter = Column(String(100), nullable=False)
    avatar = Column(String(30), nullable=False, server_default=text("''"))
    birthday = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    gender = Column(Enum(u'f', u'm'), nullable=False, server_default=text("'f'"))
    email = Column(String(90), nullable=False, server_default=text("''"))
    skype = Column(String(90), nullable=False, server_default=text("''"))
    qq = Column(String(20), nullable=False, server_default=text("''"))
    yahoo = Column(String(90), nullable=False, server_default=text("''"))
    gtalk = Column(String(90), nullable=False, server_default=text("''"))
    wangwang = Column(String(90), nullable=False, server_default=text("''"))
    mobile = Column(String(11), nullable=False, server_default=text("''"))
    phone = Column(String(20), nullable=False, server_default=text("''"))
    address = Column(String(120), nullable=False, server_default=text("''"))
    zipcode = Column(String(10), nullable=False, server_default=text("''"))
    join = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    visits = Column(Integer, nullable=False, server_default=text("'0'"))
    ip = Column(String(15), nullable=False, server_default=text("''"))
    last = Column(Integer, nullable=False, server_default=text("'0'"))
    fails = Column(Integer, nullable=False, server_default=text("'0'"))
    locked = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    ranzhi = Column(String(30), nullable=False, server_default=text("''"))
    deleted = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))


class Usercontact(db.Model):
    __tablename__ = 'usercontact'

    id = Column(Integer, primary_key=True)
    account = Column(String(30), nullable=False, index=True)
    listName = Column(String(60), nullable=False)
    userList = Column(Text, nullable=False)


t_usergroup = Table(
    'usergroup', metadata,
    Column('account', String(30), nullable=False, server_default=text("''")),
    Column('group', Integer, nullable=False, server_default=text("'0'")),
    Index('account', 'account', 'group', unique=True)
)


class Userquery(db.Model):
    __tablename__ = 'userquery'
    __table_args__ = (
        Index('query', 'account', 'module'),
    )

    id = Column(Integer, primary_key=True)
    account = Column(String(30), nullable=False)
    module = Column(String(30), nullable=False)
    title = Column(String(90), nullable=False)
    form = Column(Text, nullable=False)
    sql = Column(Text, nullable=False)


class Usertpl(db.Model):
    __tablename__ = 'usertpl'

    id = Column(Integer, primary_key=True)
    account = Column(String(30), nullable=False, index=True)
    type = Column(String(30), nullable=False)
    title = Column(String(150), nullable=False)
    content = Column(Text, nullable=False)
    public = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))
