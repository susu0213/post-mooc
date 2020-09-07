bash req-handler-ajax.sh | grep 'mArg = {' | cut -d '=' -f 2 | jq 2>/dev/null
