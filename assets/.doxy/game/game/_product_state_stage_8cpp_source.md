

# File ProductStateStage.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Sequence**](dir_c3e5e32485410daab5e4633456b74fa1.md) **>** [**ProductStateStage.cpp**](_product_state_stage_8cpp.md)

[Go to the documentation of this file](_product_state_stage_8cpp.md)


```C++
#include "Sequence/ProductStateStage.h"

#include "Sequence/ProductStageStartParam.h"

class KoopaLastStageStartParam : public ProductStageStartParam
{
public:
        virtual const char* getStageDataName()
        {
                return "KoopaLastStage";
        }
};

#ifdef NON_MATCHING
ProductStateStage::ProductStateStage( ProductSequence* parent, ProductStageStartParam* startParam, const al::LayoutInitInfo& info )
    : al::HostStateBase<ProductSequence>( parent, "ステージステート" ), mStageStartParam( startParam ),
      mLastStageStartParam( nullptr ), mStageScene( nullptr ), _1C( nullptr ), _20( nullptr ), _24( nullptr ),
      _28( nullptr ), _2C( nullptr ), _30( nullptr ), _34( nullptr ), _38( nullptr )
{
        mLastStageStartParam = new KoopaLastStageStartParam();
}

/*void ProductStateStage::init() { }
void ProductStateStage::appear() { }*/
#endif
```


