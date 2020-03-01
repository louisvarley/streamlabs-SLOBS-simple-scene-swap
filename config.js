var settings = {
  "liveOnly": false,
  "command": "!swap",
  "permission": "Everyone",
  "costs": 0,
  "delay": 30,
  "scene1": "game",
  "scene2": "cam",
  "useCooldown": true,
  "useCooldownMessages": true,
  "cooldown": 60,
  "onCooldown": "$user, $command is still on cooldown for $cd minutes!",
  "userCooldown": 300,
  "onUserCooldown": "$user, $command is still on user cooldown for $cd minutes!",
  "responseNotEnoughPoints": "$user you need $cost $currency to use $command.",
  "responseOnSuccess": "$user has called for a scene swap to $scene1 for $delay seconds."
};