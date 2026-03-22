

# File CourseSelectScene.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Scene**](dir_84f8925aa2d2bbbcb80a56e59501bb98.md) **>** [**CourseSelectScene.h**](_course_select_scene_8h.md)

[Go to the documentation of this file](_course_select_scene_8h.md)


```C++
#pragma once

#include <Scene/alScene.h>

class ProductStageStartParam;

class CourseSelectScene : public al::Scene
{
private:
        ProductStageStartParam* mStageStartParam;
        u8                      unk[ 0x34 ];

public:
        CourseSelectScene( ProductStageStartParam* stageStartParam );
};
```


