

# File ProductStateTitle.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Sequence**](dir_c3e5e32485410daab5e4633456b74fa1.md) **>** [**ProductStateTitle.cpp**](_product_state_title_8cpp.md)

[Go to the documentation of this file](_product_state_title_8cpp.md)


```C++
#include "Sequence/ProductStateTitle.h"

#include <Nerve/alNerve.h>

#include "Layout/WindowConfirmButton.h"
#include "Layout/WindowConfirmSingle.h"

namespace NrvProductStateTitle
{

NERVE_DEF( ProductStateTitle, Load )

} // namespace NrvProductStateTitle

ProductStateTitle::ProductStateTitle( ProductSequence* host, ProductStageStartParam* startParam, const al::LayoutInitInfo& info )
    : al::HostStateBase<ProductSequence>( host, "製品シーケンスのタイトルステート" ), mStartParam( startParam ),
      _1C( nullptr ), _20( nullptr ), _24( true ), _25( false )
{
        mButton = new WindowConfirmButton( "確認ウインドウ", info );
        mWindow = new WindowConfirmSingle( "確認ウインドウ[ボタン1個]", info );
}

void ProductStateTitle::init()
{
        initNerve( &NrvProductStateTitle::Load );
}
```


