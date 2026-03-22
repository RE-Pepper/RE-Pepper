

# File ProductStateCourseSelect.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Sequence**](dir_add35431d27bbd5f0559725cdc453615.md) **>** [**ProductStateCourseSelect.h**](_product_state_course_select_8h.md)

[Go to the documentation of this file](_product_state_course_select_8h.md)


```C++
#pragma once

#include <Nerve/alHostStateBase.h>

#include "Sequence/ProductSequence.h"

namespace al
{
class LayoutInitInfo;
}

class ProductStateTitle : public al::HostStateBase<ProductSequence>
{
private:
        int                     _10;
        ProductStageStartParam* mStartParam;
        void*                   _18;
        void*                   _1C;
        void*                   _20;
        void*                   _24;
        void*                   _28;
        void*                   _2C;
        void*                   _30;
        void*                   _34;
        void*                   _38;
        void*                   _3C;

public:
        void set_10( int v )
        {
                _10 = v;
        }

public:
        ProductStateTitle( ProductSequence* host, ProductStageStartParam* startParam, const al::LayoutInitInfo& info );
};
```


