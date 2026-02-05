class Camera:
  def __init__(self,camera_quality):
    self.camera_quality=camera_quality
  def display_camera_details(self):
    print("Camera quality is:",self.camera_quality)
class MusicPlayer:
  def __init__(self,sound_quality):
    self.sound_quality=sound_quality
  def display_music_details(self):
    print("Music quality is:",self.sound_quality)
class SmartPhone(Camera, MusicPlayer):
  def __init__(self, branch,camera_quality, sound_quality):
    self.branch=branch
    Camera.__init__(self,camera_quality)
    MusicPlayer.__init__(self,sound_quality)
  def display_smartphone_details(self):
      print("Smartphone Brand:", self.branch)
      self.display_camera_details()
      self.display_music_details()
phone = SmartPhone("Samsung", "108 MP", "Dolby Atmos")
phone.display_smartphone_details()

    


    