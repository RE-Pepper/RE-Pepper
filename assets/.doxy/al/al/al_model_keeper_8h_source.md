

# File alModelKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Model**](dir_b30aa7a02aee64ce0942147420d20004.md) **>** [**alModelKeeper.h**](al_model_keeper_8h.md)

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


