#include "SceneObjFactory.h"

al::SceneObj* createSceneObj(SceneObjType type) {
#define X(i, n) case i: return new N();
    switch case(type) {
        SCENE_OBJ_LIST
    };
#undef X
}

al::SceneObjHolder* SceneObjFactory::createSceneObjHolder() {
    return new al::SceneObjHolder(&sceneObjCreator, SceneObj_Max);
}
