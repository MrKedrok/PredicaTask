#!/bin/bash
set -e

case $1 in
worker*)
  shift
  exec celery -A coinscoin_lib.main worker "$@"
  ;;
management*)
  shift
  exec celery -A management_lib.main beat --loglevel=DEBUG --pidfile="/tmp/celerybeat.pid" -s /tmp/celerybeat-schedule
  ;;
justrun*)
  exec /bin/sh -c "trap : TERM INT; sleep 9999999999d & wait"
  ;;
test*)
  TEST_PATH="tests"
  if [ ! -d "$TEST_PATH" ]; then
    echo "Sorry, this image does not contain tests."
    echo "Use docker-compose to setup a complete, isolated environment."
    exit 255
  fi
  pytest --cov=coinscoin_api --cov=skidservice_lib --cov-report=term -n 3 --cov-config=.coveragerc --cov-fail-under=60 $TEST_PATH/unit/
  ;;
*)
  cat <<'###END'
    Please specify, how do you want to use this image.
    Use one of following parameters:
      worker      - run worker container
      test        - run tests
      justrun     - run container and keep it running forever
      management  - run management pod
###END
  exit 1
  ;;
esac
