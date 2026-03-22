

# File ProductStateStage.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Sequence**](dir_add35431d27bbd5f0559725cdc453615.md) **>** [**ProductStateStage.h**](_product_state_stage_8h.md)

[Go to the documentation of this file](_product_state_stage_8h.md)


```C++
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
```


