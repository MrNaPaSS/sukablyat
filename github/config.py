#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Конфигурация для Telegram бота генерации сигналов
"""

import os
from datetime import datetime
from typing import Set

class BotConfig:
    """Конфигурация Telegram бота"""
    
    # Telegram Bot Token (сигнальный бот) - ТЕСТОВЫЙ
    BOT_TOKEN = "8302370727:AAFDVRICSXe40PF5M8WR8mt4G41HPH86GTc"
    TELEGRAM_BOT_TOKEN = BOT_TOKEN  # Алиас для совместимости
    
    # Twelvedata API Keys (ротация для избежания лимитов)
    TWELVEDATA_API_KEYS = [
        "db0b6170bf88422890f72d31cde96d73",  # Новый основной ключ
        "135a5040fb4642d6be0dda33fdf12232",  # Запасной ключ 1
        "d31clt1r01qsprr0c0lgd31clt1r01qsprr0c0m0",  # Запасной ключ 2
        "your_backup_key_3",  # Запасной ключ 3 (замените на реальный)
    ]
    TWELVEDATA_API_KEY = TWELVEDATA_API_KEYS[0]  # Основной ключ для совместимости
    
    # Авторизованные пользователи (ID из Telegram)
    AUTHORIZED_USERS: Set[int] = {
        511442168,   # Ваш ID (админ)
    }
    
    # ID администратора (только для него доступен статус системы)
    ADMIN_ID = 511442168
    ADMIN_TELEGRAM_ID = ADMIN_ID  # Алиас для совместимости
    
    # Настройки генерации сигналов
    SIGNAL_SETTINGS = {
        "min_confidence": 0.5,  # Минимальная уверенность для показа сигнала
        "cache_duration": 0,    # Кэширование ОТКЛЮЧЕНО - полный анализ каждый раз
        "request_delay": 2.0,   # Задержка между запросами в секундах (увеличено)
        "max_bulk_pairs": 3,    # Максимум пар для массовой генерации (уменьшено)
        "signal_cooldown": 30,  # Задержка между генерациями сигналов (30 секунд)
        "bulk_signal_cooldown": 240, # Задержка после ТОП-3 сигналов (4 минуты)
        "api_optimization": True, # Включить оптимизацию API запросов
        "lite_mode": False,     # Облегченный режим ОТКЛЮЧЕН - используем полный анализ
    }
    
    # 6 основных форекс пар для анализа
    MAJOR_FOREX_PAIRS = [
        "EUR/USD", "GBP/USD", "USD/JPY", 
        "USD/CHF", "AUD/USD", "USD/CAD"
    ]
    
    # Настройки отображения
    DISPLAY_SETTINGS = {
        "show_detailed_indicators": True,
        "show_confidence_bar": True,
        "show_interpretation": True,
        "timezone": "Europe/Berlin",  # Часовой пояс для отображения времени
    }
    
    # Сообщения бота
    MESSAGES = {
        "welcome": (
            "🚀 <b>Добро пожаловать в систему генерации торговых сигналов!</b>\n\n"
            "🔹 <b>Возможности:</b>\n"
            "• 💱 Форекс сигналы (Пн-Пт, 06:00-22:00 CET/CEST)\n"
            "• ⚡ ОТС сигналы (круглосуточно 24/7)\n" 
            "• 📈 Технический анализ с множественными индикаторами\n"
            "• 🎯 Система скоринга качества сигналов\n"
            "• 🌐 Реальные рыночные данные\n\n"
            "👇 <b>Выберите тип торговли:</b>"
        ),
        
        "help": (
            "❓ <b>ПОМОЩЬ</b>\n\n"
            "🤖 <b>Доступные команды:</b>\n"
            "• /start - Запуск бота\n"
            "• /help - Показать помощь\n"
            "• /market - Расписание рынка\n\n"
            "📊 <b>Функции бота:</b>\n"
            "• 💱 <b>Форекс сигналы</b> - Работают в часы торгов (Пн-Пт, 06:00-22:00 CET/CEST)\n"
            "• ⚡ <b>ОТС сигналы</b> - Работают круглосуточно 24/7\n"
            "• 📈 <b>Технический анализ</b> - RSI, EMA, MACD, Bollinger Bands\n"
            "• 🎯 <b>Система скоринга</b> - Оценка качества сигналов\n\n"
            "💡 <b>Как пользоваться:</b>\n"
            "1. Выберите тип торговли (Форекс или ОТС)\n"
            "2. Выберите нужную функцию в меню\n"
            "3. Получите сигнал с детальным анализом\n\n"
            "📞 <b>Поддержка:</b> @kaktotakxm\n"
            "🔒 <b>Доступ:</b> Только для авторизованных пользователей"
        ),
        
        "market_schedule": (
            "📅 <b>РАСПИСАНИЕ РАБОТЫ РЫНКОВ</b>\n\n"
            "💱 <b>ФОРЕКС (Forex):</b>\n"
            "🕕 <b>Время работы:</b> Понедельник - Пятница\n"
            "⏰ <b>Часы:</b> 06:00 - 22:00 (CET/CEST)\n"
            "🌍 <b>Пары:</b> EUR/USD, GBP/USD, USD/JPY, USD/CHF, AUD/USD, USD/CAD\n\n"
            "⚡ <b>ОТС (Over-The-Counter):</b>\n"
            "🕐 <b>Время работы:</b> Круглосуточно 24/7\n"
            "📅 <b>Дни:</b> Понедельник - Воскресенье\n"
            "🌐 <b>Пары:</b> Те же 6 основных пар в ОТС режиме\n\n"
            "💡 <b>Примечание:</b>\n"
            "• В часы работы форекса - реальные рыночные данные\n"
            "• Вне часов форекса - демо-режим для тестирования\n"
            "• ОТС пары всегда работают с реальными данными"
        ),
        
        "unauthorized": (
            "❌ У вас нет доступа к этому боту.\n"
            "📞 Для получения доступа обратитесь: @kaktotakxm"
        ),
        
        "no_signals": (
            "⚠️ <b>Сигналы не сгенерированы</b>\n\n"
            "Возможные причины:\n"
            "• Недостаточно данных от API\n"
            "• Низкая уверенность в сигналах\n"
            "• Проблемы с подключением\n\n"
            "Попробуйте позже или проверьте статус системы."
        ),
        
        "error_general": (
            "❌ Произошла ошибка. Попробуйте позже."
        ),
        
        "generating_signal": (
            "⏳ <b>Генерация сигнала для {}...</b>\n\n"
            "Анализируем рыночные данные и технические индикаторы..."
        ),
        
        "generating_bulk": (
            "⏳ <b>Генерация сигналов для популярных пар...</b>\n\n"
            "Это может занять несколько секунд. Пожалуйста, подождите..."
        ),
        
        "risk_warning": (
            "⚠️ <b>Важно:</b> Сигналы носят информационный характер. "
            "Всегда используйте управление рисками при торговле."
        )
    }
    
    @classmethod
    def load_from_env(cls):
        """Загружает конфигурацию из переменных окружения"""
        cls.BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", cls.BOT_TOKEN)
        cls.TWELVEDATA_API_KEY = os.getenv("TWELVEDATA_API_KEY", cls.TWELVEDATA_API_KEY)
        
        # Загружаем авторизованных пользователей из переменной окружения
        env_users = os.getenv("AUTHORIZED_USERS", "")
        if env_users:
            try:
                user_ids = [int(uid.strip()) for uid in env_users.split(",") if uid.strip()]
                cls.AUTHORIZED_USERS.update(user_ids)
            except ValueError:
                print("⚠️ Ошибка парсинга AUTHORIZED_USERS из переменных окружения")
    
    @classmethod
    def add_authorized_user(cls, user_id: int):
        """Добавляет авторизованного пользователя"""
        cls.AUTHORIZED_USERS.add(user_id)
        cls._save_authorized_users()
    
    @classmethod
    def remove_authorized_user(cls, user_id: int):
        """Удаляет авторизованного пользователя"""
        cls.AUTHORIZED_USERS.discard(user_id)
        cls._save_authorized_users()
    
    @classmethod
    def _save_authorized_users(cls):
        """Сохраняет авторизованных пользователей в файл"""
        try:
            import json
            users_file = "authorized_users.json"
            data = {
                'authorized_users': list(cls.AUTHORIZED_USERS),
                'last_updated': str(datetime.now())
            }
            with open(users_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ Ошибка сохранения пользователей: {e}")
    
    @classmethod
    def _load_authorized_users(cls):
        """Загружает авторизованных пользователей из файла"""
        try:
            import json
            users_file = "authorized_users.json"
            if os.path.exists(users_file):
                with open(users_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    saved_users = data.get('authorized_users', [])
                    # Очищаем текущий список и загружаем сохраненных пользователей
                    cls.AUTHORIZED_USERS.clear()
                    cls.AUTHORIZED_USERS.update(saved_users)
                    if len(saved_users) > 0:
                        print(f"✅ Загружено {len(saved_users)} авторизованных пользователей")
        except Exception as e:
            print(f"❌ Ошибка загрузки пользователей: {e}")
    
    @classmethod
    def is_user_authorized(cls, user_id: int) -> bool:
        """Проверяет, авторизован ли пользователь"""
        return user_id in cls.AUTHORIZED_USERS


# Загружаем конфигурацию из переменных окружения при импорте
BotConfig.load_from_env()
