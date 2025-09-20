from panda3d.core import Vec3
import random


class Mobs:
    def __init__(self, pos, land, hp, speed):
        self.land = land
        self.hp = hp
        self.speed = speed
        self.direction = Vec3(1, 0, 0)

        self.hero = loader.loadModel('smiley')
        self.hero.setColor(0, 1, 0)  # зелёный, чтобы отличался от игрока
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)

        self.wander_interval = 2
        self.time_since_last_turn = 0

    def update(self, dt):
        self.time_since_last_turn += dt
        if self.time_since_last_turn > self.wander_interval:
            self.random_turn()
            self.time_since_last_turn = 0

        self.hero.setPos(self.hero.getPos() + self.direction * self.speed * dt)

        if self.hp <= 0:
            self.die()

    def random_turn(self):
        from math import sin, cos, pi
        angle = random.uniform(0, 360)
        self.direction = Vec3(cos(angle * pi / 180), sin(angle * pi / 180), 0)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        self.hero.removeNode()
