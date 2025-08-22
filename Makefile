install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall hexlet-code
