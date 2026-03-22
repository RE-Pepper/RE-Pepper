

# File alAudioKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Audio**](dir_0b6be3bddc08b0fe777b8f908ed1824a.md) **>** [**alAudioKeeper.h**](al_audio_keeper_8h.md)

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


