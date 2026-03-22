

# File EnemyStateUtil.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Enemy**](dir_e35196509c323c9bb4cd921cf1b24d53.md) **>** [**EnemyStateUtil.h**](_enemy_state_util_8h.md)

[Go to the documentation of this file](_enemy_state_util_8h.md)


```C++
#pragma once

namespace al
{
class LiveActor;
}
class EnemyStateBlowDown;

namespace EnemyStateUtil
{

bool tryRequestPressDownAndNextNerve( u32 msg, al::HitSensor* other, al::HitSensor* me, al::LiveActor* actor, const al::Nerve* nextNerve );

bool tryRequestBlowDownAndNextNerve( u32 msg, al::HitSensor* other, al::HitSensor* me, EnemyStateBlowDown* state, const al::Nerve* nextNerve );

} // namespace EnemyStateUtil
```


