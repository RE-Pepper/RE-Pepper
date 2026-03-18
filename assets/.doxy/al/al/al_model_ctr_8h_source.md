

# File alModelCtr.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Model**](dir_ab46701e979e26977414ccd9da8ce736.md) **>** [**alModelCtr.h**](al_model_ctr_8h.md)

[Go to the documentation of this file](al_model_ctr_8h.md)


```C++
#pragma once

namespace al
{
class AnimPlayerSkl;
class AnimPlayerSimple;
} // namespace al

class alModelCtr
{
private:
        void*                 _0;
        void*                 _4;
        void*                 _8;
        void*                 _C;
        void*                 _10;
        void*                 _14;
        void*                 _18;
        al::AnimPlayerSkl*    mSklAnimPlayer;
        al::AnimPlayerSimple* mMtpAnimPlayer;
        al::AnimPlayerSimple* mMtsAnimPlayer;
        al::AnimPlayerSimple* mMclAnimPlayer;
        al::AnimPlayerSimple* mVisAnimPlayer;

public:
        al::AnimPlayerSkl* getSklAnimPlayer() const
        {
                return mSklAnimPlayer;
        }

        al::AnimPlayerSimple* getMtpAnimPlayer() const
        {
                return mMtpAnimPlayer;
        }

        al::AnimPlayerSimple* getMtsAnimPlayer() const
        {
                return mMtsAnimPlayer;
        }

        al::AnimPlayerSimple* getMclAnimPlayer() const
        {
                return mMclAnimPlayer;
        }

        al::AnimPlayerSimple* getVisAnimPlayer() const
        {
                return mVisAnimPlayer;
        }
};
```


