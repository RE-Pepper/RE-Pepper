

# File ProductStateTitle.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Sequence**](dir_add35431d27bbd5f0559725cdc453615.md) **>** [**ProductStateTitle.h**](_product_state_title_8h.md)

[Go to the documentation of this file](_product_state_title_8h.md)


```C++
#pragma once

#include <Nerve/alHostStateBase.h>

#include "Sequence/ProductSequence.h"

namespace al
{
class LayoutInitInfo;
}
class WindowConfirmButton;
class WindowConfirmSingle;
class ProductStageStartParam;

class ProductStateTitle : public al::HostStateBase<ProductSequence>
{
private:
        ProductStageStartParam* mStartParam;
        WindowConfirmButton*    mButton;
        WindowConfirmSingle*    mWindow;
        void*                   _1C;
        void*                   _20;
        bool                    _24;
        bool                    _25;

public:
        ProductStateTitle( ProductSequence* host, ProductStageStartParam* startParam, const al::LayoutInitInfo& info );

        virtual void init();

        void exeLoad();
};
```


