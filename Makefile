.PHONY: start.engine
start.engine:
	@docker compose up -d

.PHONY: stop.engine
stop.engine:
	@docker compose down

.PHONY: create.index
create.index:
	@poetry run python src/scripts/create_index.py

.PHONY: delete.index
delete.index:
	@poetry run python src/scripts/delete_index.py