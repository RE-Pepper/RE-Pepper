#pragma once

#include <Nerve/alHostStateBase.h>

#include "Sequence/ProductSequence.h"

namespace al
{
class LayoutInitInfo;
}
class StageScene;
class ProductSequence;

class ProductStateStage : public al::HostStateBase<ProductSequence>
{
private:
        ProductStageStartParam* mStageStartParam;
        ProductStageStartParam* mLastStageStartParam;
        StageScene*             mStageScene;
        void*                   _1C;
        void*                   _20;
        void*                   _24;
        void*                   _28;
        void*                   _2C;
        void*                   _30;
        void*                   _34;
        void*                   _38;

public:
        // virtual void init();
        // virtual void appear();
public:
        ProductStateStage( ProductSequence* parent, ProductStageStartParam* startParam, const al::LayoutInitInfo& info );
};
