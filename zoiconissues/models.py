from flask.ext.sqlalchemy import SQLAlchemy

from zoiconissues.core import app


db = SQLAlchemy(app)


# Relate tags to issues.
issues_tags = db.Table(
    'issues_tags',
    db.Column(
        'issue_id',
        db.Integer,
        db.ForeignKey('issues.issue_id'),
        nullable=False,
    ),
    db.Column(
        'tag_id',
        db.Integer,
        db.ForeignKey('tags.tag_id'),
        nullable=False,
    ),
)


class Project(db.Model):

    __tablename__ = 'projects'

    id = db.Column(
        'project_id',
        db.Integer,
        primary_key=True)
    project = db.Column(
        db.String(64),
        nullable=False)
    active = db.Column(
        db.Boolean,
        nullable=False)

    issues = db.relationship('Issue', backref='project', lazy='dynamic')

    tags = db.relationship('Tag', lazy='select')


class Issue(db.Model):

    __tablename__ = 'issues'

    id = db.Column(
        'issue_id',
        db.Integer,
        primary_key=True)
    project_id = db.Column(
        db.Integer,
        db.ForeignKey('projects.project_id'),
        nullable=False)
    title = db.Column(
        db.String(255),
        nullable=False)

    comments = db.relationship('Comment', backref='issue', lazy='dynamic')

    tags = db.relationship(
        'Tag',
        secondary=issues_tags,
        backref=db.backref('issues', lazy='dynamic'))


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(
        'comment_id',
        db.Integer,
        primary_key=True)
    issue_id = db.Column(
        db.Integer,
        db.ForeignKey('issues.issue_id'),
        nullable=False)
    posted = db.Column(
        db.DateTime,
        nullable=False)
    comment = db.Column(
        db.Text,
        nullable=False)


class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(
        'tag_id',
        db.Integer,
        primary_key=True)
    project_id = db.Column(
        db.Integer,
        db.ForeignKey('projects.project_id'),
        nullable=False)
    tag = db.Column(
        db.String(64),
        nullable=False)
    colour = db.Column(
        db.String(6),
        nullable=False)
