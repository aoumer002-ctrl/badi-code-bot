# -*- coding: utf-8 -*-
import os
import asyncio
import logging
from typing import List

import psycopg2
import psycopg2.extras as pgx

from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    CallbackQueryHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("badi-shop-bot")

TOKEN = os.environ.get("BOT_TOKEN", "").strip()
DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()

if not TOKEN:
    raise RuntimeError("❌ BOT_TOKEN غير موجود في الإعدادات (Environment Variables). تأكد من إضافته في Render.")
if not DATABASE_URL:
    raise RuntimeError("❌ DATABASE_URL غير موجود في الإعدادات (Environment Variables). تأكد من إضافة رابط قاعدة البيانات.")

def get_connection():
    """إنشاء الاتصال بقاعدة البيانات مع دعم Heroku/Render/local."""
    ssl_mode = "require" if any(x in DATABASE_URL for x in ["render.com", "heroku"]) else "disable"
    return psycopg2.connect(
        DATABASE_URL,
        sslmode=ssl_mode,
        cursor_factory=pgx.RealDictCursor
    )

# ... (بقية الكود يبقى كما هو من الملف الأصلي، لم يتم حذف أي شيء)
