from flask_sqlalchemy import SQLAlchemy
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firts_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(120), unique=True)

    posts: Mapped[List["Post"]] = relationship(back_populates="usuario")
    comentarios: Mapped[List["Comentario"]] = relationship(back_populates="usuario")
    likes: Mapped[List["Like"]] = relationship(back_populates="usuario")


class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32), nullable=False)
    content: Mapped[str] = mapped_column(String(50), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)

    usuario: Mapped["Usuario"] = relationship(back_populates="posts")
    comentarios: Mapped[List["Comentario"]] = relationship(back_populates="post")
    likes: Mapped[List["Like"]] = relationship(back_populates="post")


class Comentario(db.Model):
    __tablename__ = "comentarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    text_comment: Mapped[str] = mapped_column(String(120))

    user_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)

    usuario: Mapped["Usuario"] = relationship(back_populates="comentarios")
    post: Mapped["Post"] = relationship(back_populates="comentarios")


class Like(db.Model):
    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)

    usuario: Mapped["Usuario"] = relationship(back_populates="likes")
    post: Mapped["Post"] = relationship(back_populates="likes")