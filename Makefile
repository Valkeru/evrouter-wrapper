INSTALL_PATH=$(HOME)/.local/bin

help:
	@echo 'install: copy ewrapper in binary dir'

install:
	cp ewrapper $(INSTALL_PATH)/
	chmod +x $(INSTALL_PATH)/ewrapper
