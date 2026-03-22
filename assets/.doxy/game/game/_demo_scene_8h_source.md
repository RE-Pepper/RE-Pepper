

# File DemoScene.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Scene**](dir_84f8925aa2d2bbbcb80a56e59501bb98.md) **>** [**DemoScene.h**](_demo_scene_8h.md)

[Go to the documentation of this file](_demo_scene_8h.md)


```C++
#pragma once

#include <Scene/alScene.h>

class PlayerActor;
class ProductStageStartParam;

class DemoScene : public al::Scene
{
private:
        ProductStageStartParam* mStageStartParam;
        PlayerActor*            mPlayerActor;
        int                     _3C;
        int                     _40;
        int                     _44;

public:
        virtual ~DemoScene();
        virtual void appear();
        virtual void kill();
        virtual void init();
        virtual void control();

public:
        DemoScene( ProductStageStartParam* stageStartParam );
};
```


