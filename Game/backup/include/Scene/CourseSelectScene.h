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
