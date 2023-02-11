from views import ArticlesView, orm_context
from aiohttp import web


app = web.Application()
app.cleanup_ctx.append(orm_context)
app.add_routes(
    [
        web.get('/articles/{article_id:\d+}', ArticlesView),
        web.patch('/articles/{article_id:\d+}', ArticlesView),
        web.delete('/articles/{article_id:\d+}', ArticlesView),
        web.post('/articles/', ArticlesView)
    ])


if __name__ == '__main__':
    web.run_app(app, port=5000)
