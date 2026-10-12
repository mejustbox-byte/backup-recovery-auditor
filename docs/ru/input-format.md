# Вход backup-1.0

Корень содержит ровно schema_version, scope, synthetic и assets. Scope — непустая строка до 128 символов; synthetic — строго boolean. Assets непустой и содержит уникальные ID до 128 символов. Полный пример — safe.synthetic.json.

Актив заявляет excessive_read, excessive_delete, encrypted, key_access_separate, immutable и immutability_verified как true, false или null. Null означает неизвестность. Это нейтральные заявления: парсер vendor ACL или retention-policy не реализован. Restore содержит ровно tested_at, result и maximum_age_days. Result — success/failure/unknown; время — UTC YYYY-MM-DDTHH:MM:SSZ либо null; maximum_age_days — целое от 1 до 3650.

[Index](index.md) · [Other language](../en/input-format.md)
