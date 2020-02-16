#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Magdalena Zubrzycka (magdalenazubrzycka1@gmail.com)

from views import app


if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=True, port=5500, use_debugger=True, use_evalex=True)
