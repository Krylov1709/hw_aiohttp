from aiohttp import web
from model import Base, Session, engine, ArticleModel
import json


async def get_article(article_id: int, session: Session):
    article = await session.get(ArticleModel, article_id)
    if article is None:
        raise web.HTTPNotFound(
            text=json.dumps({'status': 'error', 'description': 'Article not found'}),
            content_type='application/json'
        )
    return article


class ArticlesView(web.View):

    async def get(self):
        article_id = int(self.request.match_info['article_id'])
        async with Session() as session:
            article = await get_article(article_id, session)
            return web.json_response({
                'id': article.id,
                'title': article.title,
                'description': article.description,
                'creation_time': article.creation_time.isoformat()
            })

    async def post(self):
        article_data = await self.request.json()
        async with Session() as session:
            new_article = ArticleModel(**article_data)
            session.add(new_article)
            await session.commit()
            return web.json_response({
                'status': 'successfully',
                'description': 'article created'
            })

    async def patch(self):
        article_id = int(self.request.match_info['article_id'])
        article_data = await self.request.json()
        async with Session() as session:
            article = await get_article(article_id, session)
            for field, value in article_data.items():
                setattr(article, field, value)
                session.add(article)
                await session.commit()
            return web.json_response({
                'status': 'successfully',
                'description': 'article updated'
            })

    async def delete(self):
        article_id = int(self.request.match_info['article_id'])
        async with Session() as session:
            article = await get_article(article_id, session)
            await session.delete(article)
            await session.commit()
            return web.json_response({
                'status': 'successfully',
                'description': 'article delete'
            })


async def orm_context(app:web.Application):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    yield
    await engine.dispose()



