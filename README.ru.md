# Backup & Recovery Auditor

Установите bootstrap-зависимость перед пакетом. Явное UTC-время делает возраст восстановления воспроизводимым. Выходные пути не должны существовать. Коды: 0 все заявленные проверки прошли, 1 известный отказ, 2 неполные свидетельства без отказов, 3 неверный вход/выход. Неизвестность сохраняется в пробелах покрытия. Результат напрямую принимает CLI контракта отчётов.

```bash
python -m pip install -r requirements-bootstrap.txt
python -m pip install .
backup-audit examples/safe.synthetic.json --observed-at 2026-10-12T00:00:00Z --output report.json
opsec-report validate report.json
opsec-report html report.json --output report.html
```

[Documentation](docs/ru/index.md)

Локальный кандидат 0.1.0a1; hosted CI и релиз ожидаются. Реальное восстановление не выполнялось.
