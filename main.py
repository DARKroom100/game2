def on_overlap_tile(sprite, location):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_up_pressed():
    mySprite.vy += -200
    music.play(music.create_sound_effect(WaveShape.NOISE,
            5000,
            0,
            255,
            255,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile2(sprite2, location2):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        flag1
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile3)

mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . b 5 5 b . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . b b b b b 5 5 5 5 5 5 5 b . . 
            . b d 5 b 5 5 5 5 5 5 5 5 b . . 
            . . b 5 5 b 5 d 1 f 5 d 4 f . . 
            . . b d 5 5 b 1 f f 5 4 4 c . . 
            b b d b 5 5 5 d f b 4 4 4 4 b . 
            b d d c d 5 5 b 5 4 4 4 4 4 4 b 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
mySprite.set_position(10, 140)
controller.move_sprite(mySprite, 100, 0)
scene.camera_follow_sprite(mySprite)
mySprite.ay = 500