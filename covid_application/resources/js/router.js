import Vue from 'vue';
import VueRouter from 'vue-router';


Vue.use(VueRouter)

import example from './components/ExampleComponent.vue';
import trainmodel from './components/TrainModel.vue';
import UploadTestSetConfinement from './components/UploadTestSetConfinement.vue';
import Deconf from './components/Deconf.vue';
import Hybrid from './components/Hybrid.vue';
import EntrainerModel from './components/EntrainerModel.vue';

const routes = [
    {
        path: '/example',
        component: example
    },
    {
        path: '/trainmodel',
        component: trainmodel
    },
    {
        path: '/confinement',
        component: UploadTestSetConfinement
    },
    {
        path: '/deconfinement',
        component: Deconf
    },
    {
        path: '/hybride',
        component: Hybrid
    }
    ,
    {
        path: '/entrainer',
        component: EntrainerModel
    }
]

export default new VueRouter({ mode: 'history', routes: routes })