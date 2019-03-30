if [ "$UPDATE" ]
  ./update.sh && ./run_server.sh;
then
  ./run_server.sh;
fi
