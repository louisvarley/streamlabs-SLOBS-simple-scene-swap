var settings = {
  "liveOnly": false,
  "command": "!swap",
  "permission": "Everyone",
  "costs": 0,
  "delay": 15,
  "scene1": "PouchCam",
  "scene2": "Streaming Multi",
  "useCooldown": false,
  "useCooldownMessages": true,
  "cooldown": 1,
  "onCooldown": "$user, $command is still on cooldown for $cd minutes!",
  "userCooldown": 120,
  "onUserCooldown": "$user, $command is still on user cooldown for $cd minutes!",
  "responseNotEnoughPoints": "$user you need $cost $currency to use $command.",
  "responseOnSuccess": "$user has called for a scene swap."
};