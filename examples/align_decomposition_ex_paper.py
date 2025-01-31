from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.petri_net.utils.petri_utils import add_arc_from_to
from pm4py.objects.petri_net.utils import decomposition
from examples import examples_conf
import importlib.util


def execute_script():
    net = PetriNet("")
    start = PetriNet.Place("start")
    end = PetriNet.Place("end")
    c1 = PetriNet.Place("c1")
    c2 = PetriNet.Place("c2")
    c3 = PetriNet.Place("c3")
    c4 = PetriNet.Place("c4")
    c5 = PetriNet.Place("c5")
    c6 = PetriNet.Place("c6")
    c7 = PetriNet.Place("c7")
    c8 = PetriNet.Place("c8")
    c9 = PetriNet.Place("c9")
    net.places.add(c1)
    net.places.add(c2)
    net.places.add(c3)
    net.places.add(c4)
    net.places.add(c5)
    net.places.add(c6)
    net.places.add(c7)
    net.places.add(c8)
    net.places.add(c9)
    net.places.add(start)
    net.places.add(end)
    t1 = PetriNet.Transition("t1", "a")
    t2 = PetriNet.Transition("t2", None)
    t3 = PetriNet.Transition("t3", "b")
    t4 = PetriNet.Transition("t4", "c")
    t5 = PetriNet.Transition("t5", "d")
    t6 = PetriNet.Transition("t6", "e")
    t7 = PetriNet.Transition("t7", None)
    t8 = PetriNet.Transition("t8", "f")
    t9 = PetriNet.Transition("t9", "g")
    t10 = PetriNet.Transition("t10", "h")
    t11 = PetriNet.Transition("t11", None)
    net.transitions.add(t1)
    net.transitions.add(t2)
    net.transitions.add(t3)
    net.transitions.add(t4)
    net.transitions.add(t5)
    net.transitions.add(t6)
    net.transitions.add(t7)
    net.transitions.add(t8)
    net.transitions.add(t9)
    net.transitions.add(t10)
    net.transitions.add(t11)
    add_arc_from_to(start, t1, net)
    add_arc_from_to(t1, c1, net)
    add_arc_from_to(t1, c2, net)
    add_arc_from_to(c1, t2, net)
    add_arc_from_to(c1, t3, net)
    add_arc_from_to(c2, t4, net)
    add_arc_from_to(t2, c3, net)
    add_arc_from_to(t3, c3, net)
    add_arc_from_to(t4, c4, net)
    add_arc_from_to(c3, t5, net)
    add_arc_from_to(c4, t5, net)
    add_arc_from_to(t5, c5, net)
    add_arc_from_to(c5, t6, net)
    add_arc_from_to(t6, c1, net)
    add_arc_from_to(t6, c2, net)
    add_arc_from_to(c5, t7, net)
    add_arc_from_to(t7, c7, net)
    add_arc_from_to(t7, c6, net)
    add_arc_from_to(c7, t8, net)
    add_arc_from_to(c6, t9, net)
    add_arc_from_to(t8, c8, net)
    add_arc_from_to(t9, c9, net)
    add_arc_from_to(c8, t11, net)
    add_arc_from_to(c9, t11, net)
    add_arc_from_to(t11, end, net)
    add_arc_from_to(c5, t10, net)
    add_arc_from_to(t10, end, net)
    im = Marking()
    im[start] = 1
    fm = Marking()
    fm[end] = 1
    decomposed_net = decomposition.decompose(net, im, fm)
    gvizs = []

    if importlib.util.find_spec("graphviz"):
        from pm4py.visualization.petri_net import visualizer

        gvizs.append(visualizer.apply(net, im, final_marking=fm, parameters={"format": examples_conf.TARGET_IMG_FORMAT}))
        visualizer.view(gvizs[len(gvizs) - 1])
        for snet, sim, sfm in decomposed_net:
            gvizs.append(visualizer.apply(snet, sim, final_marking=sfm, parameters={"format": examples_conf.TARGET_IMG_FORMAT}))
            visualizer.view(gvizs[len(gvizs) - 1])


if __name__ == "__main__":
    execute_script()
