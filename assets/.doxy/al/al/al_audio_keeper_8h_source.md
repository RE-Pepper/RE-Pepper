

# File alAudioKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Audio**](dir_4049e994827d2af237276901db79ed98.md) **>** [**alAudioKeeper.h**](al_audio_keeper_8h.md)

[Go to the documentation of this file](al_audio_keeper_8h.md)


```C++
#pragma once

namespace al
{

class AudioKeeper
{
public:
        void update();
};

class IUseAudioKeeper
{
public:
        virtual void v1() {}
        virtual void v2() {}

        virtual AudioKeeper* getAudioKeeper() const = 0;
};

} // namespace al
```


