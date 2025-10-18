.PHONY: lint fix format check

# Ruff fix ausführen
fix:
	ruff check --fix .

# Ruff format ausführen
format:
	ruff format .

# Beides zusammen
lint: fix format

# Nur prüfen ohne zu ändern
check:
	ruff check .
	ruff format --check .

# Alles aufräumen und formatieren
clean-code: fix format
	@echo "✅ Code wurde bereinigt und formatiert!"

