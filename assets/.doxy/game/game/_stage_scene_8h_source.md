

# File StageScene.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Scene**](dir_84f8925aa2d2bbbcb80a56e59501bb98.md) **>** [**StageScene.h**](_stage_scene_8h.md)

[Go to the documentation of this file](_stage_scene_8h.md)


```C++
#pragma once

#include <Scene/alScene.h>

class PlayerActor;
class ProductStageStartParam;
class StageSceneStateGameOver;

class StageScene : public al::Scene
{
private:
        ProductStageStartParam*        mStageStartParam;
        PlayerActor*                   mPlayerActor;
        void*                          _3C;
        void*                          _40;
        void*                          _44;
        void*                          _48;
        void*                          _4C;
        void*                          _50;
        void*                          _54;
        void*                          _58;
        void*                          _5C;
        class StageSceneStateGameOver* mStateGameOver;
        void*                          _64;
        void*                          _68;
        void*                          _6C;
        void*                          _70;
        void*                          _74;
        void*                          _78;
        void*                          _7C;
        void*                          _80;
        void*                          _84;
        void*                          _88;
        void*                          _8C;
        void*                          _90;
        void*                          _94;
        void*                          _98;

public:
        virtual void appear();
        virtual void control();

public:
        StageScene( ProductStageStartParam* stageStartParam );
};
```


