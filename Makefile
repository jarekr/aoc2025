# Logging setup
# From: https://github.com/catvec/make-log/blob/master/README.md
#
NO_COLOR=\033[0m

OK_TAG=OK   #
OK_COLOR=\033[32;01m

WARN_TAG=WARN #
WARN_COLOR=\033[33;01m

ERROR_TAG=ERROR
ERROR_COLOR=\033[31;01m

define log = # level, message
$(if $(findstring ok, $(1)), @printf "$(OK_COLOR)[$(OK_TAG)] $(2)$(NO_COLOR)\n")
$(if $(findstring warn, $(1)), @printf "$(WARN_COLOR)[$(WARN_TAG)] $(2)$(NO_COLOR)\n")
$(if $(findstring error, $(1)), @printf "$(ERROR_COLOR)[$(ERROR_TAG)] $(2)$(NO_COLOR)\n")
endef

DAY=8

show: ## show current day
	@echo "Current day is ${DAY}"

test: ## run current day on test input
	@echo "Running for ${DAY} on test input ..."
	uv run python3 src/day${DAY}.py inputs/day${DAY}_testinput.txt

check: ## run current day on personalized input
	@echo "Checking solution for ${DAY}..."
	uv run python3 src/day${DAY}.py inputs/day${DAY}_input.txt

help: ## Display this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
