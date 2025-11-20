#!/usr/bin/bash

source __tinkerbell__.sh

echorun restic $HOST -r $URI dump $SNAPSHOT --tag files --target ./path/to/destination

#Voer hier je invul commando's in vanuit de service zelf.

rm -r ./restore/*
