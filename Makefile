all :
	docker compose up
down :
	docker compose down
fclean :
	docker system prune -af
re : fclean down all
	