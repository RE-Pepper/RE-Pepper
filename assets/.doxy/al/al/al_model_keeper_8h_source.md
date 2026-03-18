

# File alModelKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Model**](dir_ab46701e979e26977414ccd9da8ce736.md) **>** [**alModelKeeper.h**](al_model_keeper_8h.md)

[Go to the documentation of this file](al_model_keeper_8h.md)


```C++
#pragma once

#include <math/seadMatrix.h>

class alModelCtr;

namespace al
{

class ModelKeeper
{
private:
        alModelCtr* mModel;

public:
        alModelCtr* getModel() const
        {
                return mModel;
        }

        void hide();
};

const sead::Matrix34f* getJointMtxPtr( ModelKeeper* keeper, const char* jointName );

} // namespace al
```


