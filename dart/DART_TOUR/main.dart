class Player {
  String name = 'nico';
  int xp = 1500;
}

void main() {
  var player = Player();
  player.name = 'lalala';
  print(player.name);
}
