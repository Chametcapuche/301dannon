##
## EPITECH PROJECT, 2021
## Makefile
## File description:
## Makefile
##

MAIN				=	src/301dannon.py

MAIN_TEST			=	

EXEC_NAME			=	301dannon

RM					=	rm -rf

EXEC_NAME_TEST		=	unit_tests

all:	dannon

dannon:	$(OBJ_MAIN) $(OBJ)
	@cp $(MAIN) $(EXEC_NAME) &&	\
	(echo -e "\033[92m[DANNON OK]\033[0m" $<) || \
	(echo -e "\033[91m[DANNON NO COMPIL]\033[0m" $<; false)

tests_run:
	@cp $(MAIN_TEST) $(EXEC_NAME_TEST) &&	\
	(echo -e "\033[92m[DANNON OK]\033[0m" $<) || \
	(echo -e "\033[91m[DANNON NO COMPIL]\033[0m" $<; false)
	coverage3 run --branch unit_tests
	coverage3 report -m

clean:
	@$(RM) $(OBJ_MAIN) $(OBJ) $(OBJ_TEST) .coverage tests/.coverage

fclean:	clean
	@$(RM) $(EXEC_NAME) $(EXEC_NAME_TEST)
	@echo -e "\033[91m[RM]\033[0m Binary"

re: fclean all

.PHONY = all re clean fclean $(EXEC_NAME) $(EXEC_NAME_TEST)