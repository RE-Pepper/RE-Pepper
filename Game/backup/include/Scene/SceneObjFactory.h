#pragma once

#include <Scene/alSceneObjHolder.h>

#define SCENE_OBJ_LIST                                                         \
  X(0, CameraDirector)                                                         \
  X(1, CameraShaker)                                                           \
  //X(2, )                                                                       \
  X(3, SwitchAreaDirector)                                                     \
  X(4, SceneAudioDirector)                                                     \
  X(5, SoundEmitAreaDirector)                                                  \
  X(6, AudioVolumeSettingAreaDirector)                                         \
  X(7, CoinRotator)                                                            \
  //X(8, )                                                                       \
  //X(9, )                                                                       \
  //X(10, )                                                                       \
  //X(11, )                                                                       \
  //X(12, )                                                                       \
  //X(13, )                                                                       \
  X(14, TimerSePlayer)                                                         \
  X(15, PlayerSceneObject)                                                     \
  X(16, BlockRailDirector)                                                     \
  X(17, PatapataWingWarp)                                                      \
  X(18, PlayerItemsStorage)                                                    \
  X(20, GhostPlayerRecorder)                                                   \
  //X(21, )                                                                       \
  X(22, GyroInputReader)

class SceneObjFactory {
public:
  static al::SceneObjHolder *createSceneObjHolder();

}; // namespace SceneObjFactory


enum SceneObjType {
#define X(i, n) SceneObj_##n = i,
    SCENE_OBJ_LIST
#undef X
    SceneObj_Max
};

